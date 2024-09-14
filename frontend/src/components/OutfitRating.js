import React, { useState } from "react";
import axios from "axios";

function OutfitRating() {
  const [image, setImage] = useState(null);
  const [rating, setRating] = useState(null);

  const handleImageUpload = (e) => {
    setImage(e.target.files[0]);
  };

  const submitImage = () => {
    const formData = new FormData();
    formData.append("image", image);

    axios
      .post("http://localhost:5000/rate-outfit", formData)
      .then((response) => {
        setRating(response.data.rating);
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  };

  return (
    <div>
      <input type="file" onChange={handleImageUpload} />
      <button onClick={submitImage}>Submit Outfit</button>
      {rating && <h2>Your Outfit Rating: {rating}/100</h2>}
    </div>
  );
}

export default OutfitRating;
