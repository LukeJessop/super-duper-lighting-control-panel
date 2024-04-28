import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Salci",
  description: "FART SMELLAH"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav>
          <div>
            <div className="p-4">
              <h1>SALCI</h1>
            </div>
          </div>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
