'use client';

import React from 'react';
import { 
  FileSearch, 
  Scale, 
  BookOpen, 
  AlertOctagon, 
  FileEdit, 
  Swords, 
  SearchX, 
  Gauge, 
  Compass, 
  CheckCircle2, 
  Trophy 
} from 'lucide-react';

interface StepProgressNavProps {
  activeStep: number;
  onSelectStep: (step: number) => void;
}

const STEPS = [
  { step: 1, label: 'Fact Matrix', icon: FileSearch },
  { step: 2, label: 'Statutory Tests', icon: Scale },
  { step: 3, label: 'Precedents', icon: BookOpen },
  { step: 5, label: 'Lower Errors', icon: AlertOctagon },
  { step: 6, label: 'Submissions', icon: FileEdit },
  { step: 7, label: 'Red-Team War Room', icon: Swords },
  { step: 8, label: 'Evidence Gaps', icon: SearchX },
  { step: 9, label: 'Readiness & Viability', icon: Gauge },
  { step: 11, label: 'Forward Plan', icon: Compass },
  { step: 12, label: 'Draft Audit', icon: CheckCircle2 },
  { step: 13, label: 'Executive Verdict', icon: Trophy },
];

export const StepProgressNav: React.FC<StepProgressNavProps> = ({
  activeStep,
  onSelectStep
}) => {
  return (
    <div className="bg-white border border-beige-200 rounded-2xl p-2 mb-6 shadow-sm overflow-x-auto">
      <div className="flex items-center gap-1.5 min-w-max">
        {STEPS.map((s) => {
          const Icon = s.icon;
          const isActive = activeStep === s.step;
          return (
            <button
              key={s.step}
              onClick={() => onSelectStep(s.step)}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-xl text-xs font-medium transition-all ${
                isActive
                  ? 'bg-amber-600 text-white font-semibold shadow-sm'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-beige-50'
              }`}
            >
              <Icon className={`w-4 h-4 ${isActive ? 'text-white' : 'text-slate-400'}`} />
              <span>{s.label}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
