"use client";

import { JsonDebug } from "~/components/deer-flow/json-debug";

export default function TestJsonPage() {
  const testCases = [
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

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">🧪 Test du Parsing JSON</h1>
      
      <div className="space-y-4">
        {testCases.map((testCase, index) => (
          <div key={index} className="border rounded p-4">
            <h2 className="font-semibold mb-2">{testCase.name}</h2>
            <JsonDebug data={testCase.data} fallback={testCase.fallback} />
          </div>
        ))}
      </div>
    </div>
  );
}
