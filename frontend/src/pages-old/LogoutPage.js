import {useEffect} from "react"
import axios from "axios";


const LogoutPage = () => {
    
  useEffect(() => {
    (async () => {
      try {
        const {data} = await  
          axios.post('api/authentication/logout', 
            {refresh_token: localStorage.getItem('refresh_token')},
            {headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            }},  
            {withCredentials: true}
          );
        localStorage.clear();
        axios.defaults.headers.common['Authorization'] = null;
        window.location.href = '/login'
      } catch (e) {
        console.log('logout not working', e)
      }
    })();
  }, []);

  return (
      <div></div>
  )
}

export default LogoutPage;
