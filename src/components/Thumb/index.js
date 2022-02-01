import React from 'react';
// Styles
import { Image } from './Thumb.styles';

const Thumb = ({ image, artistId, clickable }) => (
    <div>
        <Image src={image} alt='artist-Thumb'/>
    </div>
);

export default Thumb;