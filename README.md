# simple-monitor

Example compose:
```yaml
  simple-monitor:
    container_name: simple-monitor
    build:
      context: /path/to/simple-monitor/
      dockerfile: /path/to/simple-monitor/Dockerfile
    environment:
      - WEBHOOK=https://discord.com/api/webhooks/some_discord_webhook
      - INTERVAL=3600 #optional interval, default: 3600 seconds
      - THRESHOLD=90 #optional threshold, default: 90%
    restart: always
```


Example with another disk:
```yaml
  simple-monitor:
    container_name: simple-monitor
    build:
      context: /path/to/simple-monitor/
      dockerfile: /path/to/simple-monitor/Dockerfile
    environment:
      - WEBHOOK=https://discord.com/api/webhooks/some_discord_webhook
      - INTERVAL=3600 #optional interval, default: 3600 seconds
      - THRESHOLD=90 #optional threshold, default: 90%
      - DISKS=/root,/data
    volumes:
      - /path/to/data:/data
    restart: always
```
