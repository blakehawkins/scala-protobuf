import sbt._
import Keys._

object ScalaProtoBufBuild extends Build {
  lazy val scalaProtobuf = Project("scala-protobuf", file("."), settings = mainSettings)
  lazy val mainSettings: Seq[Project.Setting[_]] = Defaults.defaultSettings ++ Seq(
  organization := "com.jeffplaisance",
  name := "scala-protobuf",
  version := "0.4",
  scalaVersion := "2.10.3",
  crossVersion := CrossVersion.binary,
  publishTo := Some(Resolver.file("Github Pages", Path.userHome / "git" / "dimbleby.github.com" / "maven" asFile)(Patterns(true, Resolver.mavenStyleBasePattern))),
  publishMavenStyle := true,
  scalacOptions ++= Seq("-deprecation", "-unchecked", "-feature")
  )
}
