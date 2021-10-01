from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Other Audience',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pysupuesto',
  version='0.2.1.0.2',
  description='Módulo para descargar bases de diferentes ejercicios (o series temporales) del presupuesto público nacional argentino desde el Ministerio de Economía',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='@Mato',
  author_email='no@email.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='presupuesto, budget', 
  packages=find_packages(),
  install_requires=[''] 
)
