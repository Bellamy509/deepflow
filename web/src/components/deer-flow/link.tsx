import { useMemo } from "react";
import { useStore, useToolCalls } from "~/core/store";
import { parseJSON } from "~/core/utils/json";
import { Tooltip } from "./tooltip";
import { WarningFilled } from "@ant-design/icons";
import { useTranslations } from "next-intl";

export const Link = ({
  href,
  children,
  checkLinkCredibility = false,
}: {
  href: string | undefined;
  children: React.ReactNode;
  checkLinkCredibility: boolean;
}) => {
  const toolCalls = useToolCalls();
  const responding = useStore((state) => state.responding);

  const credibleLinks = useMemo(() => {
    const links = new Set<string>();
    if (!checkLinkCredibility) return links;

    (toolCalls || []).forEach((call) => {
      if (call && call.name === "web_search" && call.result) {
        try {
          // Utiliser parseJSON avec une valeur de fallback sûre
          const result = parseJSON(call.result, []) as Array<{ url: string }>;
          
          if (Array.isArray(result)) {
            result.forEach((r) => {
              if (r && typeof r.url === 'string' && r.url.trim()) {
                try {
                  // encodeURI est utilisé pour gérer les caractères spéciaux
                  links.add(encodeURI(r.url));
                  links.add(r.url);
                } catch (encodeError) {
                  console.warn('Failed to encode URL:', r.url, encodeError);
                }
              }
            });
          }
        } catch (error) {
          console.warn('Failed to process web_search result:', {
            callId: call.id,
            result: call.result?.substring(0, 100) + (call.result && call.result.length > 100 ? '...' : ''),
            error: error instanceof Error ? error.message : String(error)
          });
        }
      }
    });
    return links;
  }, [toolCalls, checkLinkCredibility]);

  const isCredible = useMemo(() => {
    return checkLinkCredibility && href && !responding
      ? credibleLinks.has(href)
      : true;
  }, [credibleLinks, href, responding, checkLinkCredibility]);

  const t = useTranslations("common");
  return (
    <span className="inline-flex items-center gap-1.5">
      <a href={href} target="_blank" rel="noopener noreferrer">
        {children}
      </a>
      {!isCredible && (
        <Tooltip title={t("linkNotReliable")} delayDuration={300}>
          <WarningFilled className="text-sx transition-colors hover:!text-yellow-500" />
        </Tooltip>
      )}
    </span>
  );
};
