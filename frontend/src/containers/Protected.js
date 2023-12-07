import React, { useEffect, useState } from "react";


const Protected = (props) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  const checkUserToken = () => {
      const userToken = sessionStorage.getItem('access_token');
      if (!userToken || userToken === 'undefined') {
          setIsLoggedIn(false);
          window.location.href = '/login'
      }
      setIsLoggedIn(true);
  }
  
  useEffect(() => {
      checkUserToken();
  }, [isLoggedIn]);

  return (
      <React.Fragment>
          {
              isLoggedIn ? props.children : null
          }
      </React.Fragment>
  );
}
export default Protected;