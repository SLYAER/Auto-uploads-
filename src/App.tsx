import React, { useState } from 'react';
import { Play, FileText, Settings, Video, CheckCircle, ChevronRight, Github, Activity, AlertTriangle } from 'lucide-react';

export default function App() {
  const [step, setStep] = useState(1);

  const steps = [
    {
      title: "1. The Google Brains",
      icon: <Settings size={32} className="text-orange-400" />,
      content: (
        <div className="space-y-4">
          <p>Since you pushed the code to GitHub, the bot is self-contained. It will even download its own GTA 5 background videos automatically! It just needs permission to upload, and a brain to think of ideas.</p>
          <ol className="list-decimal pl-6 space-y-3 font-medium text-gray-300 border border-gray-800 p-6 rounded-xl bg-gray-950/50">
            <li>Open a new tab: <a href="https://console.cloud.google.com" target="_blank" className="text-blue-400 underline">console.cloud.google.com</a> (Log in with your YouTube email).</li>
            <li>Tap menu &rarr; <strong>APIs & Services</strong> &rarr; <strong>Library</strong>. Enable <strong>YouTube Data API v3</strong>.</li>
            <li>Go to <strong>OAuth consent screen</strong> (&rarr; External). Fill in required fields, save.</li>
            <li>Go to <strong>Credentials</strong> &rarr; <strong>Create Credentials</strong> &rarr; <strong>OAuth client ID</strong> (Choose "Desktop app").</li>
            <li>Download the JSON file. Rename it to exactly: <code className="text-emerald-400 bg-gray-800 px-2 py-1 rounded">credentials.json</code></li>
            <li className="pt-4 border-t border-gray-800 mt-4 text-emerald-400 font-bold">Now get the AI Brain:</li>
            <li>Go to <a href="https://aistudio.google.com/app/apikey" target="_blank" className="text-blue-400 underline">aistudio.google.com/app/apikey</a> and generate an API key. Copy it.</li>
          </ol>
        </div>
      )
    },
    {
      title: "2. Clone to Replit & Auth",
      icon: <Github size={32} className="text-purple-400" />,
      content: (
        <div className="space-y-4">
          <p>Time to run the code 24/7 in Replit and log into YouTube for the first and last time.</p>
          <ol className="list-decimal pl-6 space-y-3 font-medium text-gray-300 border border-gray-800 p-6 rounded-xl bg-gray-950/50">
            <li>Go to <a href="https://replit.com" target="_blank" className="text-blue-400 underline">Replit.com</a>. Create a new Repl and pick <strong>Import from GitHub</strong>.</li>
            <li>Paste your GitHub Repo URL and import it.</li>
            <li>In Replit, click the "Secrets" (padlock) tool on the sidebar.</li>
            <li>Add a secret named <code className="text-white bg-gray-800 px-1 rounded">GEMINI_API_KEY</code> and paste the Gemin Key you copied earlier.</li>
            <li>Upload the <code className="text-gray-400">credentials.json</code> file you generated into your Replit files.</li>
            <li>Hit the big <strong>Run</strong> button at the top!</li>
            <li><strong>WATCH THE CONSOLE:</strong> It will output a Google authorization link. Tap the link, select your YouTube account, and click Allow.</li>
            <li>Copy the auth code Google gives you, paste it into the Replit console, and hit enter. It will generate a <code>token.json</code> file.</li>
          </ol>
        </div>
      )
    },
    {
      title: "3. Connect UptimeRobot",
      icon: <Activity size={32} className="text-emerald-400" />,
      content: (
        <div className="space-y-4">
          <p>I added a secret Flask web server to your bot. We use UptimeRobot to ping this server every 5 minutes so Replit never falls asleep!</p>
          <ol className="list-decimal pl-6 space-y-3 font-medium text-gray-300 border border-gray-800 p-6 rounded-xl bg-gray-950/50">
            <li>While the bot is running in Replit, look at the "Webview" window (usually top right).</li>
            <li>It will display the text: <strong>"Bot is alive and running 24/7!"</strong></li>
            <li>Copy the web address URL from that window (it looks something like <code>https://your-bot-name.replit.app</code>).</li>
            <li>Go to <a href="https://uptimerobot.com" target="_blank" className="text-blue-400 underline">uptimerobot.com</a> and make a free account.</li>
            <li>Tap <strong>+ Add New Monitor</strong>.</li>
            <li>Monitor Type: <strong>HTTP(s)</strong></li>
            <li>URL: Paste the Replit Webview URL you just copied.</li>
            <li>Monitoring Interval: <strong>Every 5 minutes</strong>. Save!</li>
          </ol>
          <div className="mt-8 bg-emerald-900/30 border border-emerald-500/30 p-6 rounded-xl text-center">
            <h3 className="text-xl font-bold text-emerald-400 mb-2">🎉 It is fully autonomous. 🎉</h3>
            <p className="text-emerald-200">The bot downloads its own background videos, hallucinates its own titles, searches its own content, uploads to YouTube, and UptimeRobot keeps it awake forever for free.</p>
          </div>
        </div>
      )
    }
  ];

  return (
    <div className="min-h-screen bg-gray-950 text-gray-100 font-sans p-4 md:p-8 overflow-y-auto">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-10">
          <h1 className="text-3xl font-bold text-white mb-3">The Super Simple Guide</h1>
          <p className="text-gray-400">Take a deep breath. We will do this one tiny step at a time.</p>
        </div>

        {/* Vercel Warning */}
        <div className="bg-red-900/20 border border-red-500/30 p-6 rounded-2xl mb-8 flex gap-4 text-left shadow-lg shadow-red-900/10">
          <AlertTriangle className="text-red-400 shrink-0" size={32} />
          <div>
            <h3 className="text-xl font-bold text-red-400 mb-2">Can I use Vercel?</h3>
            <p className="text-red-200">
              <strong>No, Vercel will completely fail.</strong> Vercel is built for websites, not 24/7 background video-rendering bots. It has a strict 10-second timeout and a read-only hard drive, which means the python bot cannot render or save the heavy MP4 video files. You <strong>must</strong> use Replit (with UptimeRobot), Render, Railway, or a real VPS server.
            </p>
          </div>
        </div>

        <div className="bg-gray-900 border border-gray-800 rounded-2xl shadow-2xl overflow-hidden">
          {/* Progress Bar */}
          <div className="flex border-b border-gray-800">
            {steps.map((s, i) => (
              <button
                key={i}
                onClick={() => setStep(i + 1)}
                className={`flex-1 py-3 text-center text-sm font-bold transition-colors ${
                  step === i + 1 
                    ? 'bg-blue-600 border-b-2 border-blue-400 text-white' 
                    : step > i + 1
                      ? 'bg-emerald-900/40 text-emerald-400'
                      : 'bg-gray-900 text-gray-500'
                }`}
              >
                {step > i + 1 ? <CheckCircle size={16} className="mx-auto" /> : i + 1}
              </button>
            ))}
          </div>

          <div className="p-8 md:p-10">
            <div className="flex items-center gap-4 mb-6">
              {steps[step - 1].icon}
              <h2 className="text-2xl font-bold text-white">{steps[step - 1].title}</h2>
            </div>
            
            <div className="text-lg leading-relaxed">
              {steps[step - 1].content}
            </div>

            <div className="mt-10 flex justify-between items-center border-t border-gray-800 pt-6">
              <button 
                onClick={() => setStep(Math.max(1, step - 1))}
                disabled={step === 1}
                className={`px-6 py-3 rounded-lg font-bold ${step === 1 ? 'opacity-0 cursor-default' : 'bg-gray-800 text-gray-300 hover:bg-gray-700'}`}
              >
                Back
              </button>
              
              {step < steps.length && (
                <button 
                  onClick={() => setStep(Math.min(steps.length, step + 1))}
                  className="px-6 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-lg font-bold flex items-center gap-2 shadow-lg shadow-blue-900/50"
                >
                  I'm done with this step <ChevronRight size={20} />
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
