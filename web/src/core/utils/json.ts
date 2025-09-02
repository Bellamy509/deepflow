import { parse } from "best-effort-json-parser";

export function parseJSON<T>(json: string | null | undefined, fallback: T): T {
  if (!json) {
    return fallback;
  }
  
  try {
    const raw = json
      .trim()
      .replace(/^```json\s*/, "")
      .replace(/^```js\s*/, "")
      .replace(/^```ts\s*/, "")
      .replace(/^```plaintext\s*/, "")
      .replace(/^```\s*/, "")
      .replace(/\s*```$/, "");
    
    // Vérifier si la chaîne est vide après nettoyage
    if (!raw.trim()) {
      console.warn('parseJSON: Empty string after cleaning');
      return fallback;
    }
    
    // Essayer de parser avec la bibliothèque best-effort
    const result = parse(raw);
    
    // Vérifier si le résultat est valide
    if (result === undefined || result === null) {
      console.warn('parseJSON: Parsed result is null/undefined, using fallback');
      return fallback;
    }
    
    return result as T;
    
  } catch (error) {
    console.warn('parseJSON: Failed to parse JSON:', {
      original: json?.substring(0, 100) + (json && json.length > 100 ? '...' : ''),
      error: error instanceof Error ? error.message : String(error)
    });
    return fallback;
  }
}
