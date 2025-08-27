import React from "react";
import { SignIn, SignUp, SignedIn, SignedOut } from "@clerk/clerk-react";
export default function AuthenticatioPage() {
  return (
    <div className="auth-container">
      <SignedIn>
        <div className="redirect-message">
          <p>You are signed in!</p>
        </div>
      </SignedIn>
      <SignedOut>
        <SignIn routing="path" path="/sign-in" />
        <SignUp routing="path" path="/sign-up" />
      </SignedOut>
    </div>
  );
}
