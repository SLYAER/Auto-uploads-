import React from 'react';
import { AlertTriangle, Download, Server, XCircle } from 'lucide-react';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans flex text-left p-4 overflow-y-auto">
      <div className="max-w-2xl w-full mx-auto bg-gray-900 border border-gray-800 p-8 rounded-2xl shadow-2xl h-fit my-auto">
        
        <div className="flex items-center gap-4 mb-6 pb-6 border-b border-gray-800">
          <div className="bg-red-500/20 p-3 rounded-full text-red-500">
            <XCircle size={32} />
          </div>
          <div>
            <h1 className="text-2xl font-bold text-white">I Cannot Run This Code For You</h1>
            <p className="text-gray-400 mt-1">A clarification of my AI capabilities.</p>
          </div>
        </div>

        <div className="space-y-6 text-gray-300 leading-relaxed text-lg">
          <p>
            Ah, I understand now! You are looking for a system that acts as an <strong className="text-white">autonomous personal assistant</strong> to physically find, edit, and upload videos directly to your YouTube channel on your behalf right now.
          </p>

          <div className="bg-blue-900/20 border border-blue-900/50 p-5 rounded-xl text-blue-200">
            <p className="font-semibold text-blue-400 mb-2 flex items-center gap-2">
               <AlertTriangle size={20} /> What I actually am:
            </p>
            <p className="text-sm">
              I am an AI <strong>Coding Assistant</strong> inside Google AI Studio. I can write the exact Python scripts needed for this process, but <strong className="text-white">I cannot physically execute them for you.</strong> I don't have a video rendering engine, I cannot securely login to your YouTube account, and my processing server shuts down immediately when you close this browser tab.
            </p>
          </div>

          <p>
            To make your automated channel a reality, you have to take the code I just wrote for you and run it on a computer or a cloud server.
          </p>

          <div className="bg-gray-950 p-5 rounded-xl border border-gray-800 mt-8">
            <h3 className="font-semibold text-emerald-400 mb-4 flex items-center gap-2">
              <Download size={20} /> What you need to do next:
            </h3>
            <ol className="list-decimal pl-5 space-y-4 text-sm text-gray-400">
              <li>Look at the top-left corner of this screen and click the <strong>Files / Code Explorer</strong> icon.</li>
              <li>Click the three dots/settings icon next to your project name and select <strong>"Export to ZIP"</strong> to download the bot to your phone.</li>
              <li>You must run this file on a real computer or upload it to <strong>GitHub</strong> or a <strong>VPS</strong> (like I outlined in the previous steps) so it can run 24/7 on its own!</li>
            </ol>
          </div>
        </div>

      </div>
    </div>
  );
}
