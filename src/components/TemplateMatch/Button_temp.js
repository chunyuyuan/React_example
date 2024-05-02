import styled from "styled-components"


export const ButtonContainer1 =  styled.button`
text-transorm: capitalize;
font-size: 10px;
background: transparent;
border: none;
color: var(--mainBlue);
border-radius: 0 rem;

cursor: pointer;
margin: 0 auto;

transition: all 0.5s ease-in-out;
&:hover{
    background:var(--mainYellow);
    color:white;

}
&:focus{
    outline:none;
}

`