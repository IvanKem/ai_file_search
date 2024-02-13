✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  wKh+jDvM_s38BLAhU=Jx

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  61658391dcfc815aa95cc674fdc6938cd8657b5e74c9be6c3f05ed86169c28b6

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjEyLjEiLCJhZHIiOlsiMTcyLjE5LjAuMjo5MjAwIl0sImZnciI6IjYxNjU4MzkxZGNmYzgxNWFhOTVjYzY3NGZkYzY5MzhjZDg2NTdiNWU3NGM5YmU2YzNmMDVlZDg2MTY5YzI4YjYiLCJrZXkiOiJGX1l2bzQwQm1jbUhmaWR2M1pVRDpYWVFsMEo1OVRxcXJNLTY3Q2dyT1RRIn0=

ℹ️ Configure other nodes to join this cluster:
• Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjEyLjEiLCJhZHIiOlsiMTcyLjE5LjAuMjo5MjAwIl0sImZnciI6IjYxNjU4MzkxZGNmYzgxNWFhOTVjYzY3NGZkYzY5MzhjZDg2NTdiNWU3NGM5YmU2YzNmMDVlZDg2MTY5YzI4YjYiLCJrZXkiOiJGZll2bzQwQm1jbUhmaWR2M1pVQzo2VWRlZ0RiTVFDQ29nZlJoMXpUZkFRIn0=

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.12.1`
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

http_ca.crt Successfully copied 3.58kB to /home/iv.kem/.
