import React, { Component } from 'react';
class CollegesList extends Component {
    state = {

        colleges: null
    }
    // getCookie(name) {
    //     var regexp = new RegExp("(?:^" + name + "|;\s*"+ name + ")=(.*?)(?:;|$)", "g");
    //     var result = regexp.exec(document.cookie);
    //     return (result === null) ? null : result[1];
    //   }
    getCook(cookiename) {
        // Get name followed by anything except a semicolon
        var cookiestring = RegExp("" + cookiename + "[^;]+").exec(document.cookie);
        // Return everything after the equal sign, or an empty string if the cookie name not found
        return decodeURIComponent(!!cookiestring ? cookiestring.toString().replace(/^[^=]+./, "") : "");
    }

    componentDidMount() {

        fetch('https://127.0.0.1:8000/api/colleges/', {
            headers: {
                Authorization: `JWT ${this.getCook('jwt')}`

            }
        })
            .then(response => response.json())
            .then(collegelist => {
                console.log(collegelist);
                this.setState({
                    colleges: collegelist,

                });
            });
        console.log('Here');
        console.log(this.state.colleges);
    }



    render() {
        console.log('Render');
        console.log(this.state.colleges);
        return (
            <div>
                      
                                <table class="table table-dark">
                                    {/* p key={curr.id}>{curr.name}</p> */}
                                    <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>Location</th>
                                            <th>Acronym</th>
                                            <th>Conatct</th>
                                        </tr>
                                    </thead>
                                    <tbody>

                {

                    this.state.colleges && this.state.colleges.map((curr) => {
                        return (
                      
                                        <tr>
                                            <td>{curr.name}</td>
                                            <td>{curr.location}</td>
                                            <td>{curr.acronym}</td>
                                            <td>{curr.contact}</td>
                                        </tr>
                                   );
                    }
                    )
                }
                 </tbody>

</table>
</div>
           

        );
    }
}
export default CollegesList;