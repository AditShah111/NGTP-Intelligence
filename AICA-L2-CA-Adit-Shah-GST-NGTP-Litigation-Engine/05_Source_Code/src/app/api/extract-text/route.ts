import { NextResponse } from 'next/server';
import mammoth from 'mammoth';

export const dynamic = 'force-dynamic';

export async function POST(req: Request) {
  try {
    const formData = await req.formData();
    const file = formData.get('file') as File | null;

    if (!file) {
      return NextResponse.json({ success: false, error: 'No file provided' }, { status: 400 });
    }

    const filename = file.name.toLowerCase();
    const arrayBuffer = await file.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);

    let extractedText = '';

    if (filename.endsWith('.docx') || filename.endsWith('.doc')) {
      // Clean Microsoft Word extraction via mammoth
      const result = await mammoth.extractRawText({ buffer });
      extractedText = result.value || '';
    } else if (filename.endsWith('.pdf')) {
      // PDF text extraction
      try {
        const { PDFParse } = require('pdf-parse');
        const parser = new PDFParse(new Uint8Array(buffer));
        const res = await parser.getText();
        extractedText = res.text || '';
      } catch (pdfErr: any) {
        console.warn('pdf-parse error:', pdfErr.message);
        extractedText = `[PDF Document: ${file.name} - ${(file.size / 1024).toFixed(1)} KB]`;
      }
    } else {
      // Plain text formats (.txt, .md, .csv, .json)
      extractedText = buffer.toString('utf-8');
    }

    // Clean up excessive whitespace while preserving paragraphs
    const cleanedText = extractedText
      .replace(/\r\n/g, '\n')
      .replace(/[ \t]+/g, ' ')
      .replace(/\n{3,}/g, '\n\n')
      .trim();

    return NextResponse.json({
      success: true,
      filename: file.name,
      characterCount: cleanedText.length,
      text: cleanedText
    });
  } catch (err: any) {
    console.error('Extract text failed:', err);
    return NextResponse.json({
      success: false,
      error: err.message || 'Failed to extract text from file'
    }, { status: 500 });
  }
}