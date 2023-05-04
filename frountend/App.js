import React from "react";
import Navbar from "./components/Navbar.js";
import Table from "./components/Table.js";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Delete from "./components/Delete.js";
import Verified from "./components/Verified.js";
import Login from "./components/Login.js";
import Logout from "./components/Logout.js";
import History from "./components/History.js";




function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
        <Route path="/" element={<Login />} />
        <Route exact path="/Table" element={<Table />} />
        <Route exact path="/Verified" element={<Verified />} />
        <Route exact path="/Delete" element={<Delete />} />
        <Route exact path="/Logout" element={<Logout />} />
        <Route exact path="/History" element={<History />} />
        
        </Routes>
        
      </Router>
    </>
  );
}

export default App;
