const dns = require('dns');
try {
  dns.setDefaultResultOrder('ipv4first');
} catch (e) {}

const { createServer } = require('http');
const { parse } = require('url');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const hostname = '0.0.0.0';
const port = parseInt(process.env.PORT || '10000', 10);

const app = next({ dev, hostname, port });
const handle = app.getRequestHandler();

console.log(`Preparing Next.js server on port ${port}...`);

app.prepare().then(() => {
  const server = createServer(async (req, res) => {
    try {
      const parsedUrl = parse(req.url, true);
      
      // Fast path health check
      if (parsedUrl.pathname === '/healthz' || parsedUrl.pathname === '/api/health') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ 
          status: 'healthy', 
          engine: 'NGTP Litigation Readiness & Viability Engine',
          version: '1.0.0',
          timestamp: new Date().toISOString() 
        }));
        return;
      }

      await handle(req, res, parsedUrl);
    } catch (err) {
      console.error('Error occurred handling', req.url, err);
      res.statusCode = 500;
      res.end('internal server error');
    }
  });

  server.listen(port, hostname, (err) => {
    if (err) throw err;
    console.log(`> 🚀 NGTP Litigation Engine ready on http://${hostname}:${port}`);
  });
}).catch((err) => {
  console.error('Server startup error:', err);
  process.exit(1);
});