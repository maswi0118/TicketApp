import React from 'react';
// Styles
import { Image } from './Thumb.styles';

const Thumb = ({ image, eventName, artistName, date, genre, price }) => (
    <div>
        <Image src={image} alt='artist-Thumb'/>
        <h3>{eventName}</h3>
        <h3>{artistName}</h3>
        <h4>{date}</h4>
        <h4>{genre}</h4>
        <h3>{price} PLN</h3>
        <a href={localStorage.getItem("logged") == "true" ? "/" : "/profile"}>Buy now</a>
    </div>
);

export default Thumb;