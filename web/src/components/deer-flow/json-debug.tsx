import { parseJSON } from "~/core/utils/json";

interface JsonDebugProps {
  data: string | null | undefined;
  fallback: any;
}

export const JsonDebug = ({ data, fallback }: JsonDebugProps) => {
  const parsed = parseJSON(data, fallback);
  
  return (
    <div className="p-4 border rounded bg-gray-50">
      <h3 className="font-bold mb-2">JSON Debug</h3>
      <div className="text-sm">
        <div><strong>Original:</strong> {data ? `"${data.substring(0, 100)}${data.length > 100 ? '...' : ''}"` : 'null'}</div>
        <div><strong>Parsed:</strong> {JSON.stringify(parsed, null, 2)}</div>
        <div><strong>Type:</strong> {typeof parsed}</div>
        <div><strong>Is Array:</strong> {Array.isArray(parsed)}</div>
      </div>
    </div>
  );
};
