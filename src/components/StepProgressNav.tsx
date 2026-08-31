'use client';

import React from 'react';
import { 
  Table, 
  Scale, 
  BookOpen, 
  AlertOctagon, 
  FileEdit, 
  Swords, 
  Search, 
  Gauge, 
  Navigation, 
  CheckSquare, 
  Gavel
} from 'lucide-react';

interface StepProgressNavProps {
  activeStep: number;
  onSelectStep: (step: number) => void;
}

export const StepProgressNav: React.FC<StepProgressNavProps> = ({
  activeStep,
  onSelectStep
}) => {
  const steps = [
    { num: 1, label: 'Fact Matrix', icon: Table },
    { num: 2, label: 'Statutory Engine', icon: Scale },
    { num: 3, label: 'Precedents & Score', icon: BookOpen },
    { num: 5, label: 'Lower Authority Errors', icon: AlertOctagon },
    { num: 6, label: 'Submission Optimizer', icon: FileEdit },
    { num: 7, label: 'Red-Team Adversary', icon: Swords },
    { num: 8, label: 'Evidence Gaps', icon: Search },
    { num: 9, label: 'Readiness & Viability', icon: Gauge },
    { num: 11, label: 'Forward Decision', icon: Navigation },
    { num: 12, label: 'Draft Audit', icon: CheckSquare },
    { num: 13, label: 'Final Evaluator Verdict', icon: Gavel },
  ];

  return (
    <div className="flex items-center gap-1.5 overflow-x-auto pb-3 mb-5 border-b border-legal-800/60 scrollbar-thin">
      {steps.map((s) => {
        const Icon = s.icon;
        const isActive = activeStep === s.num;
        return (
          <button
            key={s.num}
            onClick={() => onSelectStep(s.num)}
            className={`flex items-center gap-2 px-3 py-2 rounded-lg text-xs font-medium whitespace-nowrap transition-all ${
              isActive
                ? 'bg-amber-500 text-black font-semibold shadow-md shadow-amber-500/20'
                : 'bg-legal-900/80 hover:bg-legal-800 text-slate-300 border border-legal-800/80 hover:border-legal-700'
            }`}
          >
            <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-black' : 'text-amber-400'}`} />
            <span>Step {s.num}: {s.label}</span>
          </button>
        );
      })}
    </div>
  );
};
