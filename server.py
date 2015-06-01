#-------------------------------------------------------------------------------
import web
import json

#-------------------------------------------------------------------------------
urls = (
    '/jobs', 'Jobs',
    '/jobs/(.*)', 'Job'
)

app = web.application( urls, globals() )

#-------------------------------------------------------------------------------
class Jobs:
    def GET( self ):
        request = {}
        try:
            request = json.loads( web.data() )
        except ValueError:
            print "error : decoding json request"

        print request

        ret = {'ok': False, 'errormsg': "Not Implemented" }
        web.header('Content-Type', 'applicacion/json')
        return json.dumps(ret)

    def PUT( self ):
        request = {}
        try:
            request = json.loads( web.data() )
        except ValueError:
            print "error : decoding json request"

        print request

        ret = {'ok': False, 'errormsg': "Not Implemented" }
        web.header('Content-Type', 'applicacion/json')
        return json.dumps(ret)

#-------------------------------------------------------------------------------
class Job:
    def GET( self, job ):
        ret = {'ok': False, 'errormsg': "Not Implemented" }
        web.header('Content-Type', 'applicacion/json')
        return json.dumps(ret)        

    def POST( self, job ):
        request = {}
        try:
            request = json.loads( web.data() )
        except ValueError:
            print "error : decoding json request"

        print request
        ret = {'ok': False, 'errormsg': "Not Implemented" }
        web.header('Content-Type', 'applicacion/json')
        return json.dumps(ret)        
        
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run()

#-------------------------------------------------------------------------------
