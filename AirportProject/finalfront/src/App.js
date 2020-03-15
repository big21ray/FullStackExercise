import React, {Component} from 'react';
import './App.css';
import {Column} from 'react-virtualized';
import { Header} from 'semantic-ui-react'

import 'react-virtualized/styles.css'; // only needs to be imported onceimport axios from 'axios';
import axios from 'axios';

import styled from 'styled-components'

import VirtualizedTable from './VirtualizedTable'
import Paginator from './Paginator'


const Wrapper = styled.div`
  margin: 10px;
`


class App extends Component{
  constructor(props) {  
    super(props);
    
    
    this.state = {

      perPage: 25,
      currentPage:0,
      scrollToIndex: undefined ,
      offset :0,
      contacts: [],
      headers : ['ReportPeriod','Terminal','Arrival_Departure','Domestic_International','Passenger_Count'],  
  
    }
    this.handleRowsScroll = this.handleRowsScroll.bind(this);
    this.handlePageChange = this.handlePageChange.bind(this) ;
  
    }

    handleRowsScroll({ stopIndex }) {
      this.setState(prevState => {
        const page = Math.ceil(stopIndex / prevState.perPage)
        return { page, scrollToIndex: undefined }
      })
    }

    handlePageChange(page) {
      this.setState(prevState => {
        const scrollToIndex = (page - 1) * prevState.perPage
        return { page, scrollToIndex }
      })
    }
      


  componentDidMount() {
    
    axios.get('http://localhost:8000/api/original/')
    
    .then((res) => {

    let el = res.data;
    for(var i = 0; i<el.length;i++){
      el[i]['key'] = i;
    };
    


  
      
    this.setState({loading: true,
    contacts:el,
    rows : res.data.length, 

  })
    
    
    
    })
   
    

      
    
    .catch(console.log);
  }
  


  render(){
    const { page, perPage, scrollToIndex } = this.state

    const headerHeight = 30
    const rowHeight = 40
    const height = rowHeight * perPage + headerHeight
    const rowCount = this.state.contacts.length
    const pageCount = Math.ceil(rowCount / perPage)


      
        return(  



          <Wrapper>
        <Header as='h1'>Airport Instances</Header>
        <p>
          <Paginator
            pageCount={pageCount}
            currentPage={page}
            onPageChange={this.handlePageChange}
          />
        </p>
        <VirtualizedTable
          rowHeight={rowHeight}
          headerHeight={headerHeight}
          height={height}
          rowCount={this.state.contacts.length}
          rows={this.state.contacts}
          onRowsRendered={this.handleRowsScroll}
          scrollToIndex={scrollToIndex}
          scrollToAlignment='start'
        >
          <Column label='Id' dataKey='key' width={100} /> 
          <Column label='ReportPeriod' dataKey='ReportPeriod' width={1000} /> 
          <Column label='Terminal' dataKey='Terminal' width={250} /> 
          <Column label='Arrival_Departure' dataKey='Arrival_Departure' width={1000} />
          <Column label='Domestic_International' dataKey='Domestic_International' width={1000} />
          <Column label='Passenger_Count' dataKey='Passenger_Count' width={1000} />
        </VirtualizedTable>
      </Wrapper>
        )
        
        
        
      
      
        

    
  }
}



export default App;
