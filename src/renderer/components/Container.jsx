import React from "react";

export default function Container({ children }) {
    return (
        <div className="max-w-screen-lg mx-auto my-0 px-4">
            {children}
        </div>
    );
}
