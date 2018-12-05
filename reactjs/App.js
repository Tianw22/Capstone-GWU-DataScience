import React from 'react';
import ReactDOM from 'react-dom';
import Calendarhorizontal from './calendarreleasebyday'; //引入js文件
import BoxRadial from './boxradialboxofficebyday';
import Piemultidonuts from './donutrank';
import Wordcloud from './wordcloud';
import Stepseries from './stepchart';

class Intl extends React.Component{
    constructor(props){
        super(props);
            this.state = {
            };
    }

    componentDidMount(){ 

    }

    render() {
        return (
    <div>
        <h2>Launch by day</h2>
        <Calendarhorizontal/>
        <h2>Box office by month</h2>
        <BoxRadial/>
        <h2>Score by month</h2>
        <Piemultidonuts/>
        <h2>Genre</h2>
        <Wordcloud/>
        <h2>Box-office vs grade</h2>
        <Stepseries/>
    </div>

        ); 
  }
}
export default Intl;
