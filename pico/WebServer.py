from phew import server, access_point, dns
from phew.template import render_template
from phew.server import file_exists, FileResponse, Response

class WebServer:
    def __init__(self, apSettings):
        @server.route("/", methods=['GET'])
        def index(request):
            return render_template("httpdocs/index.html")
            
        @server.route("/passwords", methods=['GET'])
        def passwords(request):
            return FileResponse('passwords.csv')
            
        @server.route("/update/before", methods=['GET'])
        def updateBefore(request):
            file = open('passwords.csv', 'w')

            file.write("")
            file.close()

            return Response("", 200)
            
        @server.route("/update/append", methods=['POST'])
        def updateAppend(request):
            file = open('passwords.csv', 'a')

            line = ""

            line += request.form.get("title", "")
            line += "\t"

            line += request.form.get("username", "")
            line += "\t"

            line += request.form.get("password", "")
            line += "\n"

            file.write(line)
            file.close()

            return Response("", 200)

        @server.catchall()
        def catchall(request):
            filePath = f"httpdocs{request.path}"

            if file_exists(filePath):
                return FileResponse(filePath)
        
        accessPoint = access_point(apSettings.ssid, apSettings.password)
        ip = accessPoint.ifconfig()[0]
        
        dns.run_catchall(ip)
        server.run()