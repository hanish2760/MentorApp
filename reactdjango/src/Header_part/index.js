import React,{Component} from 'react';
class HeaderPart extends Component{
    state ={
        isloggedIn:this.props.isLoggedIn
    }
    // constructor(props){

    //     super(props);
    //     this.state={
    //   isLoggedIn : this.props.isLoggedIn 
    //     };
    // }

    toggleLoggedIn =  () => {
        this.setState(prev =>({
            isLoggedIn: !prev.isLoggedIn
        }))
}
    checkLoginStatus=() => {
          
    }
    render(){
        const {title}=this.props;
        const {isLoggedIn}=this.state;
        console.log(this.props);
        return( 
        
                <div>
                    <h2>{title}</h2>
                    <div onClick={this.toggleLoggedIn}>
                    {
                        isLoggedIn ? <span>  logout </span>: <span>login</span>
                  }
                        
                    </div>
                </div>
            );  
    }



}
export default HeaderPart