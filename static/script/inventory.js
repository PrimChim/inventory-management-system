fetch("http://localhost:8000/api/products/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((element) => {
      document.getElementById("producttable").innerHTML +=
        "<tr>" +
        "<td>" +
        element["id"] +
        "</td>" +
        "<td>" +
        element["name"] +
        "</td>" +
        "<td>" +
        element["quantity"] +
        "</td>" +
        "<td>" +
        element["location"] +
        "</td>" +
        "<td>" +
        element["reorderpoint"] +
        "</td>" +
        "<td>" +
        element["created_date"] +
        "</td>" +
        "<td>" +
        element["price"] +
        "</td>" +
        "<td>" +
        element["expirationdate"] +
        "</td>" +
        "<td>" +
        element["brand"] +
        "</td>" +
        "<td></td></tr>";
    });
  })
  .catch((error) => {
    console.error("Error:", error);
  });
