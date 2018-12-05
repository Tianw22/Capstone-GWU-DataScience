import React from 'react';
import ReactDOM from 'react-dom';
import Calendarhorizontal from './calendar每日票房'; //引入js文件
import BoxRadial from './boxradial每月票房';
import Piemultidonuts from './donut评分';
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
