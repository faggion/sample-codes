YUI.add('gallery-querystring', function(Y) {

    /**
     *  Client-side access to querystring name=value pairs
     *  License (Simplified BSD):
     *  http://adamv.com/dev/javascript/qslicense.txt
    */
    var Q = function (qs) { // optionally pass a querystring to parse
        Q.superclass.constructor.apply(this);
        this._parse(qs);
    }
    
    Q.NAME = 'querystring';
    Y.extend(Q, Y.Base, {
        params: {},
        _parse: function(qs){
            if (qs == null) qs = location.search.substring(1, location.search.length);
            if (qs.length == 0) return;
            
            // Turn <plus> back to <space>
            // See: http://www.w3.org/TR/REC-html40/interact/forms.html#h-17.13.4.1
            qs = qs.replace(/\+/g, ' ');
            var args = qs.split('&'); // parse out name/value pairs separated via &
            
            // split out each name=value pair
            for (var i = 0; i < args.length; i++) {
                var pair = args[i].split('=');
                var name = decodeURIComponent(pair[0]);
                var value = (pair.length==2)
                    ? decodeURIComponent(pair[1])
                    : name;
                this.params[name] = value;
            }
        },
        initializer: function(){},
        destructor: function(){},
        get: function(key, default_) {
            var value = this.params[key];
            return (value != null) ? value : default_;
        },
        contains: function(key) {
            var value = this.params[key];
            return (value != null);
        }
    });
    
    Y.querystring = Q;


}, '@VERSION@' ,{requires:['node', 'event']});
