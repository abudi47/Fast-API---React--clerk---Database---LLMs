import React from "react";
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";
import { Outlet, Link, Navigate } from "react-router-dom";
export default function LayOut() {
  return (
    <div className="app-layout">
      <header className="app-header">
        <div className="header-content">
          <h1>Code Challenge Generator </h1>
          <nav>
            <SignedIn>
              <Link to="/"> Generate Challenge</Link>
              <Link to="/history"> History</Link>
              <UserButton />
            </SignedIn>
          </nav>
        </div>
      </header>
    </div>
  );
}
