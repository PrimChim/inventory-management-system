let productTable = document.getElementById("producttable");

fetch("http://localhost:8000/api/products/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((element) => {
      const tr = document.createElement("tr");

      const td1 = document.createElement("td");
      td1.textContent = element["id"];
      td1.style.textAlign = "center";
      tr.appendChild(td1);

      const td2 = document.createElement("td");
      td2.textContent = element["name"];
      td2.style.textAlign = "center";
      tr.appendChild(td2);

      const td3 = document.createElement("td");
      td3.textContent = element["quantity"];
      td3.style.textAlign = "center";
      tr.appendChild(td3);

      const td4 = document.createElement("td");
      td4.textContent = element["location"];
      td4.style.textAlign = "center";
      tr.appendChild(td4);

      const td5 = document.createElement("td");
      td5.textContent = element["reorderpoint"];
      td5.style.textAlign = "center";
      tr.appendChild(td5);

      const td6 = document.createElement("td");
      td6.textContent = element["created_at"];
      td6.style.textAlign = "center";
      tr.appendChild(td6);

      const td7 = document.createElement("td");
      td7.textContent = element["price"];
      td7.style.textAlign = "center";
      tr.appendChild(td7);

      const td8 = document.createElement("td");
      td8.textContent = element["expirationdate"];
      td8.style.textAlign = "center";
      tr.appendChild(td8);

      const td9 = document.createElement("td");
      td9.textContent = element["brand"];
      td9.style.textAlign = "center";
      tr.appendChild(td9);

      const td10 = document.createElement("td");

      const editImg = document.createElement("img");
      editImg.setAttribute(
        "src",
        "http://localhost:8000/static/Image/edit2.png"
      );
      editImg.setAttribute("alt", "Edit");
      editImg.style.width = "20px";
      editImg.style.height = "20px";
      editImg.style.left = "0";
      editImg.style.top = "0";
      editImg.style.position = "relative";

      const deleteImg = document.createElement("img");
      deleteImg.setAttribute(
        "src",
        "http://localhost:8000/static/Image/delete2.png"
      );
      deleteImg.setAttribute("alt", "Delete");
      deleteImg.style.width = "20px";
      deleteImg.style.height = "20px";
      deleteImg.style.left = "10px";
      deleteImg.style.top = "0";
      deleteImg.style.position = "relative";

      td10.appendChild(editImg);
      td10.appendChild(deleteImg);
      td10.style.textAlign = "center";

      tr.appendChild(td10);

      productTable.appendChild(tr);
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });
