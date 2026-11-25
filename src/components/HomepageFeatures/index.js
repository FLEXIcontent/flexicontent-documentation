import clsx from 'clsx';
import Translate from '@docusaurus/Translate';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: (
      <Translate id="homepage.feature.cck.title">A CCK for Joomla!</Translate>
    ),
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <Translate id="homepage.feature.cck.description">
        FLEXIcontent extends Joomla!'s native article, category and tag management without replacing the core components.
      </Translate>
    ),
  },
  {
    title: <Translate id="homepage.feature.fields.title">Types and fields</Translate>,
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <Translate id="homepage.feature.fields.description">
        Structure your content with custom types and reusable fields, single or multi-valued.
      </Translate>
    ),
  },
  {
    title: (
      <Translate id="homepage.feature.display.title">
        Custom display
      </Translate>
    ),
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <Translate id="homepage.feature.display.description">
        Templates, modules and faceted filters let you build views tailored to each project.
      </Translate>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
