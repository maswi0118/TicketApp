import React from 'react';
// Styles
import { Image } from './Ticket.styles';

const Ticket = ({ image, eventName, artistName, date, genre, id}) => {
        return(
            <div>
                <Image src={image} alt='artist-pic'/>
                <h3>{eventName}</h3>
                <h3>{artistName}</h3>
                <h4>{date}</h4>
                <h4>{genre}</h4>
                <h4>Ticket id: {id}</h4>
            </div>
        )
};

export default Ticket;