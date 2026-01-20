import React from "react";
import Container from "./Container";

export default function Header({ children }) {
   return (
      <header className="absolute top-0 left-0 w-full">
         <Container>
            <div className="min-h-[60px] flex items-center">
               {children}
            </div>
         </Container>
      </header>
   );
}
