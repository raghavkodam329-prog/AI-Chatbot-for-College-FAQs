Write-Host "Starting Loyola Academy AI Chatbot..."
Write-Host "Logs will be saved to app.log"
python app.py 2>&1 | Tee-Object -FilePath app.log
