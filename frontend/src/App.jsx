import ClerkProviderWithRoutes from "./auth/ClerkProviderWithRoutes";
import { Routes, Route } from "react-router-dom";
import LayOut from "./layout/LayOut";
import ChallengeGenerator from "./challenges/challengeGenerator";
import MCQChallenge from "./challenges/MCQChallenge";
import AuthenticatioPage from "./auth/AuthenticatioPage";
import HistoryPanel from "./history/HistoryPanel";

import "./App.css";

function App() {
  return (
    <ClerkProviderWithRoutes>
      <Routes>
        <Route path="/sign-in/*" element={<AuthenticatioPage />} />
        <Route path="/sign-up" element={<AuthenticatioPage />} />
        <Route element={<LayOut />}>
          <Route path="/" element={<ChallengeGenerator />} />
          <Route path="/mcq" element={<MCQChallenge />} />
          <Route path="/history" element={<HistoryPanel />} />
        </Route>
      </Routes>
    </ClerkProviderWithRoutes>
  );
}

export default App;
