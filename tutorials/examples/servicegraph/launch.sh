
#!/bin/bash
ls -la /shared
cd /shared
curl -Lo video.mp4 $1
go2rtc -config /shared/go2rtc.yaml
exit
