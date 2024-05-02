import styled from "styled-components"


export const ButtonContainer =  styled.button`
text-transorm: capitalize;
font-size: 15px;
background: transparent;
border:0.08rem solid var(--mainBlue);
color: var(--mainBlue);
border-radius: 0.5rem;
padding : 0.1rem 0.2rem;
cursor: pointer;
margin: 0 0.2rem 0.1rem 0.1rem;

transition: all 0.5s ease-in-out;
&:hover{
    background:var(--mainYellow);
    color:white;

}
&:focus{
    outline:none;
}

`