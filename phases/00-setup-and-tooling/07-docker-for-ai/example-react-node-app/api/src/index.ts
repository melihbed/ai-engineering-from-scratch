import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json([
    {
      id: 1,
      name: "Product 1",
      priceCent: 1200,
    },
    {
      id: 2,
      name: "Product 2",
      priceCent: 1100,
    },
  ]);
});

app.listen(8000, () => {
  console.log("Server running on http://localhost:8000");
});
