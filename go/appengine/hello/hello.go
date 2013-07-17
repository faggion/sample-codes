package hello

import (
	"fmt"
	"net/http"
	"appengine"
)

func init() {
	http.HandleFunc("/", hello)
}

func hello(w http.ResponseWriter, r *http.Request) {
	c := appengine.NewContext(r)
	c.Infof("Requested URL: %v", r.URL)
	c.Debugf("this is debug message")
	c.Errorf("this is error message")
	c.Warningf("this is warning message")
	c.Criticalf("this is critical message")

	c.Debugf("request header = %v", r.Header)
	c.Debugf("user agent = %v", r.Header["User-Agent"])
	fmt.Fprintf(w, "<h1>Hello, world</h1>")
}
