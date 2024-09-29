import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    authUrl: "https://0775881.propelauthtest.com",
    integrationApiKey: "1788a70793f45b993cdc78f005852f9564a0742ea7fec4aeb8885bbf15ecab46c48e9ce2ad2c4ffae78b42d674c50ebf",
    proxyPort: 8000,
    urlWhereYourProxyIsRunning: 'http://localhost:8000',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})