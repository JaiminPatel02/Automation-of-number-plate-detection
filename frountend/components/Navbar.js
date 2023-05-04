import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { Menu } from "antd";
import "../navbar.css";
import logo from "../images/notification.gif";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";


function Navbar() {
  const [data1, setdata1] = useState([]);
  const [data, setdata] = useState([]);
  const [selectedKey, setSelectedKey] = useState("home");
  const [username, setUsername] = useState("");
  const auth = localStorage.getItem("userdata");
  useEffect(() => {
    localdata();
    axios.get();
  }, []);
  //data local
  async function localdata() {
   
    try {
      const data = await axios.get(
        `http://127.0.0.1:5000/count/${JSON.parse(auth).Username}`
      );
      setdata(data.data.count);
      console.log(data.data.count);
    } catch (e) {
      console.log(e);
    }
  }

  const logout = () => {
    localStorage.clear();
  };
function toss(){
  toast(`Remain  notification is ${data} `);

}
 

 
  const Compare = localStorage.getItem("userdata1");
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`http://127.0.0.1:5000/count/${JSON.parse(auth).Username}`);
      const newData = await response.json();
      setdata1(newData);
    };

    fetchData();

    const intervalId = setInterval(fetchData, 5000);
    return () => clearInterval(intervalId);
  }, []);
  return (
    <>
      {auth ? (
        <nav>
        <div  style={{ display: "flex-box" }}>
          <Menu
            className="topnav"
            theme="light"
            mode="horizontal"
            selectedKeys={[selectedKey]}
            onClick={({ key }) => setSelectedKey(key)}
          >
            <Menu.Item
              key="home"
              className="menu-item"
              style={
                selectedKey === "home"
                  ? { backgroundColor: "rgb(105, 181, 231)", color: "black" }
                  : null
              }
            >
              <Link to="/Table" className="testd">
                Home
              </Link>
            </Menu.Item>
           
            <Menu.Item
              key="verified"
              className="menu-item"
              style={
                selectedKey === "verified"
                  ? { backgroundColor: "rgb(105, 181, 231)", color: "black" }
                  : null
              }
            > 
              <Link to="/Verified">Verified</Link>
            </Menu.Item>
            {/* <Menu.Item key="login" className="menu-item" style={selectedKey === "login" ? {backgroundColor: 'rgb(105, 181, 231)', color: 'black'} : null}>
          <Link to="/Login">Login</Link>
        </Menu.Item> */}
            <Menu.Item
              key="delete"
              className="menu-item"
              style={
                selectedKey === "delete"
                  ? { backgroundColor: "rgb(105, 181, 231)", color: "black" }
                  : null
              }
            >
              <Link to="/Delete">Deleted</Link>
            </Menu.Item>
            <Menu.Item
          key="history"
          className="menu-item"
          style={
            selectedKey === "history"
              ? { backgroundColor: "rgb(105, 181, 231)", color: "black" }
              : null
          }
        >
          <Link to="/History">History</Link>
     
        </Menu.Item>

        
            <Menu.Item
             key="Logout"
          className="menu-item"
          style={
            selectedKey === "Logout"
              ? { backgroundColor: "rgb(105, 181, 231)", color: "black" }
              : null
          }>
              <Link className="logout" to="/" onClick={logout}>
                Logout
              </Link>
            </Menu.Item>
            <Link to="/Table">
              <img className="ghantdi" onClick={toss} src={logo} alt="loading..." />
              <span class="notifications-count"  >{data}</span>

            <ToastContainer
                            position="top-right"
                            autoClose={500}                           
                            closeOnClick                          
                            draggable                            
                            theme="dark"
                          />
            </Link>
          </Menu>
        </div>
        </nav>
      ) : null}
    </>
  );
}

export default Navbar;
