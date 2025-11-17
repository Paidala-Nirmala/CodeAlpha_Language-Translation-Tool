import React, { useState } from 'react';

function Translator() {
  const [input, setInput] = useState('');
  const [sourceLang, setSourceLang] = useState('en');
  const [targetLang, setTargetLang] = useState('es');
  const [translated, setTranslated] = useState('');
  
  const handleTranslate = async () => {
    // Example uses Google Translate API v2. Use an actual API endpoint & secure key
    const apiKey = 'YOUR_API_KEY'; // Never store real keys in client code for production!
    const url = `https://translation.googleapis.com/language/translate/v2?key=${apiKey}`;
    const body = {
      q: input,
      source: sourceLang,
      target: targetLang,
      format: 'text'
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await response.json();
    if (data && data.data && data.data.translations[0]) {
      setTranslated(data.data.translations[0].translatedText);
    } else {
      setTranslated('Translation not available.');
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(translated);
  };

  const handleSpeak = () => {
    if ('speechSynthesis' in window) {
      const utter = new SpeechSynthesisUtterance(translated);
      utter.lang = targetLang;
      window.speechSynthesis.speak(utter);
    }
  };

  return (
    <div style={{ maxWidth: 500, margin: '0 auto', padding: 24 }}>
      <textarea
        value={input}
        onChange={e => setInput(e.target.value)}
        placeholder="Enter text to translate"
        style={{ width: '100%', height: 80 }}
      />
      <div style={{ margin: '12px 0' }}>
        <label>
          Source:
          <select value={sourceLang} onChange={e => setSourceLang(e.target.value)}>
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="fr">French</option>
            {/* Add more languages as needed */}
          </select>
        </label>
        <label style={{ marginLeft: 16 }}>
          Target:
          <select value={targetLang} onChange={e => setTargetLang(e.target.value)}>
            <option value="es">Spanish</option>
            <option value="en">English</option>
            <option value="fr">French</option>
            {/* Add more languages as needed */}
          </select>
        </label>
        <button onClick={handleTranslate} style={{ marginLeft: 16 }}>Translate</button>
      </div>
      <div style={{ border: '1px solid #ccc', minHeight: 50, padding: 10 }}>
        {translated}
      </div>
      <div style={{ marginTop: 8 }}>
        <button onClick={handleCopy}>Copy</button>
        <button onClick={handleSpeak} style={{ marginLeft: 8 }}>Speak</button>
      </div>
    </div>
  );
}

export default Translator;
