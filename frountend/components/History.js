import "../table.css";
import "../navbar.css";
import axios from "axios";
import React, { useState, useEffect } from "react";
function History() {
  const [data1, setdata1] = useState([]);
  const [data, setdata] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [filteredData, setFilteredData] = useState([]);
  const [sortOrder, setSortOrder] = useState("asc");
  const auth = localStorage.getItem("userdata")
  useEffect(() => {
    localdata();
    axios.get();
  }, []);

 
  //data local
  async function localdata() {
    try {
      const data = await axios.get(`http://127.0.0.1:5000/fetchv/${JSON.parse(auth).Username}`);
      setdata(data.data.data);
    } catch (e) {
      console.log(e);
    }
  }

  
//search
  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
  };
  useEffect(() => {
    setFilteredData(
      data.filter((dataa) => {
        return (
          dataa.location.toLowerCase().includes(searchTerm.toLowerCase()) ||
          dataa.time.toLowerCase().includes(searchTerm.toLowerCase()) ||
          dataa.mac_address.toLowerCase().includes(searchTerm.toLowerCase())
        );
      })
    );
  }, [searchTerm, data]);
  
  //short
  const sortData = () => {
    const sortedData = [...data];
    if (sortOrder === "asc") {
      sortedData.sort((a, b) => (a.date > b.date ? 1 : -1));
      setSortOrder("desc");
    } else {
      sortedData.sort((a, b) => (a.date < b.date ? 1 : -1));
      setSortOrder("asc");
    }

    setdata(sortedData);
  };
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`http://127.0.0.1:5000/fetch/${JSON.parse(auth).Username}`);
      const newData = await response.json();
      setdata1(newData);
    };

    fetchData();

    const intervalId = setInterval(fetchData, 5000);
    return () => clearInterval(intervalId);
  }, []);
  return (
    <>
     <div className="tbbar">
     <img className="search_icon" src="https://img.icons8.com/ios-filled/18/null/search--v1.png"/>

        <input
          className="search"
          type="text"
          placeholder="Search..."
          onChange={handleSearch}
        />
       
      </div>
      <div id="table-users">
        {" "}
        <table>
          <thead >
            <tr>
              <th className="History">No</th>
              <th className="History">Date <button className="short" onClick={sortData}>
                  {sortOrder === "asc" ? "▲" : "▼"}</button></th>
              <th className="History">Time</th>
              <th className="History">MAC Address</th>
              <th className="History">Location</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.map((dataa, inx) => {
              return (
                <>
                  <tr>
                    <td>{inx + 1}</td>                  
                    <td>{dataa.date}</td>
                    <td>{dataa.time}</td>
                    <td>{dataa.mac_address}</td>
                    <td>{dataa.location}</td>
                  </tr>
                </>
              );
            })}
          </tbody>
        </table>
      </div>
    
    </>
  );
}
/**/

export default History;
