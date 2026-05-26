import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    fetch("http://localhost:8000")
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);
  return (
    <>
      <h1>Products</h1>
      <div className="products">
        {products.map((product) => (
          <div key={product.id} className="product">
            <h2>{product.name}</h2>
            <span>${product.priceCent}</span>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
