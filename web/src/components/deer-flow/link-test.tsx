"use client";

import { Link } from "./link";

interface LinkTestProps {
  href: string;
  children: React.ReactNode;
}

export const LinkTest = ({ href, children }: LinkTestProps) => {
  return (
    <div className="p-4 border rounded bg-blue-50">
      <h3 className="font-bold mb-2">Test Link Component</h3>
      <div className="mb-2">
        <strong>URL:</strong> {href}
      </div>
      <div className="mb-2">
        <strong>Link:</strong> <Link href={href} checkLinkCredibility={true}>{children}</Link>
      </div>
    </div>
  );
};
