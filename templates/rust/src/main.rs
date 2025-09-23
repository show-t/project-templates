use anyhow::Result;
use dotenvy;
use tracing_subscriber::{self, EnvFilter};
use tracing_subscriber::fmt::time::LocalTime;

fn tracing_init() -> Result<()> {
    dotenvy::dotenv()?;

    tracing_subscriber::fmt()
        .with_timer(LocalTime::rfc_3339())
        .with_env_filter(EnvFilter::from_default_env())
        .init();

    Ok(())

}

#[tokio::main]
async fn main() -> Result<()> {
    _ = tracing_init()?;

    println!("Hello, world!");

    Ok(())

}
