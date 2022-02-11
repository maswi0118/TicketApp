import React from 'react';
// Styles
import { Image } from './Thumb.styles';
import {usePurchase} from "../../hooks/usePurchase";
import Button from "../Button";


const Thumb = ({ image, eventName, artistName, date, genre, price, eid }) => {
        const { setIsPurchasing, setEid } = usePurchase();
        return(
            <div>
                <Image src={image} alt='artist-Thumb'/>
                <h3>{eventName}</h3>
                <h3>{artistName}</h3>
                <h4>{date}</h4>
                <h4>{genre}</h4>
                <h3>{price} PLN</h3>
                <Button text={'Buy ticket'} callback={() => {setIsPurchasing(true); setEid(eid)}}/>
        </div>
        )
};

export default Thumb;