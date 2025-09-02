"use client";

import { JsonDebug } from "~/components/deer-flow/json-debug";
import { LinkTest } from "~/components/deer-flow/link-test";

export default function DebugPage() {
  const jsonTestCases = [
    {
      name: "JSON valide simple",
      data: '{"url": "https://example.com", "title": "Test"}',
      fallback: []
    },
    {
      name: "JSON avec backticks",
      data: '```json\n{"url": "https://example.com"}\n```',
      fallback: []
    },
    {
      name: "JSON malformé",
      data: '{"url": "https://example.com", "title": "Test"',
      fallback: []
    },
    {
      name: "Chaîne vide",
      data: "",
      fallback: []
    },
    {
      name: "Chaîne avec caractères spéciaux",
      data: '{"url": "https://example.com/测试", "title": "Test"}',
      fallback: []
    }
  ];

  const linkTestCases = [
    {
      href: "https://example.com",
      children: "Example.com"
    },
    {
      href: "https://google.com",
      children: "Google"
    },
    {
      href: "https://github.com",
      children: "GitHub"
    }
  ];

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-8">🐛 Page de Debug DeerFlow</h1>
      
      {/* Section JSON Parsing */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">🧪 Test du Parsing JSON</h2>
        <div className="space-y-4">
          {jsonTestCases.map((testCase, index) => (
            <div key={index} className="border rounded p-4">
              <h3 className="font-semibold mb-2">{testCase.name}</h3>
              <JsonDebug data={testCase.data} fallback={testCase.fallback} />
            </div>
          ))}
        </div>
      </section>

      {/* Section Link Component */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">🔗 Test du Composant Link</h2>
        <div className="space-y-4">
          {linkTestCases.map((testCase, index) => (
            <LinkTest key={index} href={testCase.href}>
              {testCase.children}
            </LinkTest>
          ))}
        </div>
      </section>

      {/* Section Informations Système */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">ℹ️ Informations Système</h2>
        <div className="border rounded p-4 bg-gray-50">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div><strong>User Agent:</strong> {navigator.userAgent}</div>
            <div><strong>Platform:</strong> {navigator.platform}</div>
            <div><strong>Language:</strong> {navigator.language}</div>
            <div><strong>Cookies Enabled:</strong> {navigator.cookieEnabled ? 'Oui' : 'Non'}</div>
          </div>
        </div>
      </section>

      {/* Section Console Logs */}
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">📝 Console Logs</h2>
        <div className="border rounded p-4 bg-black text-green-400 font-mono text-sm">
          <div>Ouvrez la console du navigateur (F12) pour voir les logs</div>
          <div>Les erreurs de parsing JSON seront affichées ici</div>
        </div>
      </section>
    </div>
  );
}
