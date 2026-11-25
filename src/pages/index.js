import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Translate, {translate} from '@docusaurus/Translate';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          <Translate id="homepage.title">FLEXIcontent Documentation</Translate>
        </Heading>
        <p className="hero__subtitle">
          <Translate id="homepage.tagline">The advanced CCK for Joomla!</Translate>
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            <Translate id="homepage.cta.discover">
              Discover FLEXIcontent
            </Translate>
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="/docs/demarrage/installation">
            <Translate id="homepage.cta.install">Install</Translate>
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title={translate({
        id: 'homepage.meta.title',
        message: 'FLEXIcontent Documentation',
      })}
      description={translate({
        id: 'homepage.meta.description',
        message: 'Documentation for the FLEXIcontent CCK for Joomla!',
      })}>
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
