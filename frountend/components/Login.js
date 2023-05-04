import React, { useState } from "react";

// import "../navbar.css";
import "../login.css";
import { useNavigate } from "react-router-dom";
import axios from "axios";
const Login = () => {
  const [email, setEmail] = useState([]);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const handleSubmit = async (event) => {
    event.preventDefault();
    console.warn("jp");
    console.warn(username); 
    const response = await axios.get(
      `http://127.0.0.1:5000/valid/${username}/${password}`
    );
    const data = response.data;

    console.log(response.data.status);

    if (response.data.status === "Yes") {
      navigate("/Table");
      window.location.reload();
      console.log("Yes me gusaa");
      if (response.data.Username === "admin") {
        console.log("admin");
        navigate("/Table");
        localStorage.setItem("userdata", JSON.stringify(response.data));
        localStorage.setItem("userdata1", JSON.stringify(response.data));
        console.log( localStorage.getItem("Username"))
      } else if (response.data.Username === "Gota") {
        console.log("Gota");
        navigate("/Table");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Ranip") {
        console.log("Ranip");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Bapunagar") {
        console.log("Bapunagar");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Bopal") {
        console.log("Bopal");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Kalupur") {
        console.log("Kalupur");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Naroda") {
        console.log("Naroda");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Nikol") {
        console.log("Nikol");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Pirana") {
        console.log("Pirana");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Sarkhej") {
        console.log("Sarkhej");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "Thaltej") {
        console.log("Thaltej");
        localStorage.setItem("userdata", JSON.stringify(response.data));
      } else if (response.data.Username === "lol") {
        console.log("lol");
      } else {
        console.log("Kuch bhi bhai ?");
      }
    } else {
      console.log("No,,,,,NO Betaaaa");
    }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div className="bg-login" id="bg-login2">
          <div className="login">
            <div className="login-container">
              {/* {error && <p style={{ color: "red" }}>{error}</p>} */}
              <h3>Login</h3>
              <br/>
              <div className="txt">Username</div>
              <div>
                <input
                  className="Email"
                  type="text"
                  id="username"
                  placeholder=" Username..."
                  value={username}
                  onChange={(event) => setUsername(event.target.value)}
                />
              </div>
              <br/>
              <div>
                <div className="txt">Password</div>

                <input
                  className="Password"
                  type="password"
                  id="password"
                  placeholder=" Password..."
                  value={password}
                  onChange={(event) => setPassword(event.target.value)}
                />
                <br/><br/><br/>

                <label>
                  <input type="checkbox" checked="checked" name="remember" />{" "}
                  Remember me
                </label>

                <div className="forgot">
                  <a href="#">Forgot Password?</a>
                </div>
                
              </div>
              <button variant="primary" className="bt-login" type="submit">
                Login
              </button>
            </div>
            <div className="side-img"></div>
          </div>
        </div>
      </form>
    </>
  );
};

export default Login;
//recf
